<script setup>
import { ref, computed, watch, onMounted } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme, toggleDarkMode, setDarkMode } = appStore;

import HeaderButton from "./HeaderButton.vue";
import SideMenu from "./SideMenu.vue";
import SideMenuEntry from "./SideMenuEntry.vue";
import SideMenuSection from "./SideMenuSection.vue";
import SideMenuBanner from "./SideMenuBanner.vue";

const appWidth = ref(window.innerWidth);
const appHeight = ref(window.innerHeight);

window.addEventListener("resize", () => {
  appWidth.value = document.getElementById("app").offsetWidth;
  appHeight.value = document.getElementById("app").offsetHeight;
});

const headerHeight = 40;

const sideMenuOpen = ref(false);
const userMenuOpen = ref(false);

watch(sideMenuOpen, () => {
  if (sideMenuOpen.value) {
    userMenuOpen.value = false;
  }
});

watch(userMenuOpen, () => {
  if (userMenuOpen.value) {
    sideMenuOpen.value = false;
  }
});

const menuExpandLimit = 600;

const sideMenuWidth = computed(() => {
  return appWidth.value < menuExpandLimit ? "100%" : "250px";
});

const userMenuWidth = computed(() => {
  return appWidth.value < menuExpandLimit ? "100%" : "initial";
});

const userMenuHeight = computed(() => {
  return appWidth.value < menuExpandLimit ? "100%" : "initial";
});

const isDarkModeEnabled = localStorage.getItem("citheron.darkModeEnabled");
if (isDarkModeEnabled !== null) {
  setDarkMode(isDarkModeEnabled === "true");
} else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
  setDarkMode(true);
}

function closeMenus() {
  sideMenuOpen.value = false;
  userMenuOpen.value = false;
}

const sideMenuBannerCaption = ref("");
const sideMenuPreviousSection = ref("");

function changeSideMenuSection(name) {
  const sideMenu = document.getElementById("side-menu");
  const sideMenuSections = sideMenu.getElementsByClassName("side-menu-section");
  Array.prototype.forEach.call(sideMenuSections, (element) => {
    element.style.display = "none";
    if (element.getAttribute("data-side-menu-section-name") == name) {
      element.style.display = "initial";
      sideMenuBannerCaption.value = element.getAttribute("data-side-menu-section-caption");
      sideMenuPreviousSection.value = element.getAttribute("data-side-menu-section-back");
    }
  });
}

function previousSideMenuSection() {
  const prev = sideMenuPreviousSection.value;
  if (prev) changeSideMenuSection(prev);
}

onMounted(() => {
  changeSideMenuSection("apps");
});
</script>

<template>
  <div id="dashboard-page">
    <header>
      <HeaderButton v-bind:icon="sideMenuOpen ? 'MenuOpen' : 'Menu'" v-on:click="sideMenuOpen = !sideMenuOpen" />
      <HeaderButton icon="AccountCircle" float="right" v-on:click="userMenuOpen = !userMenuOpen" />
      <HeaderButton icon="Notifications" float="right" counter="42" />
      <HeaderButton v-bind:icon="appStore.darkModeEnabled ? 'DarkMode' : 'LightMode'" v-on:click="toggleDarkMode()" float="right" />
    </header>

    <main v-on:click="closeMenus()">
    </main>

    <SideMenu id="side-menu" v-bind:width="sideMenuWidth" v-bind:height="`${appHeight - headerHeight}px`" v-bind:top="`${headerHeight}px`" entrydash="left" v-bind:open="sideMenuOpen">
      <SideMenuBanner v-bind:caption="sideMenuBannerCaption" buttonLeftIcon="Back" :buttonLeftAction="previousSideMenuSection" buttonRightIcon="Pin" />
      <SideMenuSection name="apps" caption="Applications">
        <SideMenuEntry label="Notes" icon="Book" />
        <SideMenuEntry label="Tasks" icon="Task" />
        <SideMenuEntry label="Vaults" icon="Vault" />
        <SideMenuEntry label="Administration" icon="Server" v-on:click="changeSideMenuSection('admin')" />
        <SideMenuEntry label="Settings" icon="Settings" />
      </SideMenuSection>
      <SideMenuSection name="admin" caption="Administration" back="apps">
        <SideMenuEntry label="Users" icon="Person" />
      </SideMenuSection>
    </SideMenu>

    <SideMenu id="user-menu" v-bind:width="userMenuWidth" v-bind:height="userMenuHeight" position="right" entryDash="false" v-bind:top="`${headerHeight}px`" v-bind:open="userMenuOpen">
      <SideMenuEntry label="Help" icon="Help" />
      <SideMenuEntry label="About" icon="Info" />
      <SideMenuEntry label="Logout" icon="Logout" />
    </SideMenu>
  </div>
</template>

<style scoped>
#dashboard-page {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  width: 100%;
  height: v-bind("`${headerHeight}px`");
  background-color: v-bind("theme.headerBackgroundColor");
}

main {
  flex: 1;
  background-color: v-bind("theme.mainBackgroundColor");
}
</style>
