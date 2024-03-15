<script setup>
import { ref, computed, onMounted } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme, toggleDarkMode } = appStore;

import NavBar from "./NavBar.vue";
import NavBarButton from "./NavBarButton.vue";
import SideMenu from "./SideMenu.vue";
import SideMenuEntry from "./SideMenuEntry.vue";
import SideMenuSection from "./SideMenuSection.vue";
import SideMenuBanner from "./SideMenuBanner.vue";

import DemoPanel from "./panels/DemoPanel.vue";
import UserPanel from "./panels/UserPanel.vue";

const appWidth = ref(window.innerWidth);
const appHeight = ref(window.innerHeight);

window.addEventListener("resize", () => {
  appWidth.value = document.getElementById("app").offsetWidth;
  appHeight.value = document.getElementById("app").offsetHeight;
});

const headerHeight = 42; // TODO: replace

const sideMenuOpen = ref(false);
const userMenuOpen = ref(false);

const sideMenuPinned = ref(false);

const menuExpandLimit = 600;

const menusExpanded = computed(() => {
  return appWidth.value < menuExpandLimit;
});

const sideMenuWidth = computed(() => {
  return menusExpanded.value ? "100%" : "250px";
});

const userMenuWidth = computed(() => {
  return menusExpanded.value ? "100%" : "initial";
});

const userMenuHeight = computed(() => {
  return menusExpanded.value ? "100%" : "initial";
});

function closeMenus() {
  if (!sideMenuPinned.value)
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
    <NavBar>
      <NavBarButton
          v-bind:icon="sideMenuOpen ? 'menu-open' : 'menu'"
          v-on:click="sideMenuOpen = !sideMenuOpen"
          v-bind:active="sideMenuOpen" />
      <NavBarButton
          icon="user-circle"
          float="right"
          v-on:click="userMenuOpen = !userMenuOpen"
          v-bind:active="userMenuOpen" />
      <NavBarButton icon="bell" float="right" counter="42" />
      <NavBarButton
          v-bind:icon="appStore.darkModeEnabled ? 'dark' : 'light'"
          v-on:click="toggleDarkMode()"
          float="right" />
    </NavBar>

    <main v-if="!(menusExpanded && sideMenuOpen)" v-on:click="closeMenus()">
      <!-- <DemoPanel /> -->
      <UserPanel />
    </main>

    <SideMenu id="side-menu" v-bind:width="sideMenuWidth" v-bind:height="`${appHeight - headerHeight}px`" v-bind:top="`${headerHeight}px`" entry-dash="left" v-bind:open="sideMenuOpen">
      <SideMenuBanner
        v-bind:caption="sideMenuBannerCaption"
        v-bind:button-left-active="sideMenuPreviousSection"
        v-bind:button-right-active="!menusExpanded"
        button-left-icon="chevron-left"
        v-bind:button-right-icon="sideMenuPinned ? 'pin-off' : 'pin'"
        :button-left-action="previousSideMenuSection"
        :button-right-action="() => {sideMenuPinned = !sideMenuPinned}" />
      <SideMenuSection name="apps">
        <SideMenuEntry label="Notes" icon="book" />
        <SideMenuEntry label="Tasks" icon="task" />
        <SideMenuEntry label="Vault" icon="vault" />
        <SideMenuEntry label="Administration" icon="server" v-on:click="changeSideMenuSection('admin')" />
        <SideMenuEntry label="Settings" icon="gear" v-on:click="changeSideMenuSection('settings')" />
      </SideMenuSection>
      <SideMenuSection name="admin" caption="Administration" back="apps">
        <SideMenuEntry label="Users" icon="user" />
        <SideMenuEntry label="Groups" icon="group" />
        <SideMenuEntry label="Authentication" icon="key" />
      </SideMenuSection>
      <SideMenuSection name="settings" caption="Settings" back="apps">
      </SideMenuSection>
    </SideMenu>

    <SideMenu id="user-menu" v-bind:width="userMenuWidth" v-bind:height="userMenuHeight" position="right" entryDash="none" v-bind:top="`${headerHeight}px`" v-bind:open="userMenuOpen">
      <SideMenuEntry label="Help" icon="help" />
      <SideMenuEntry label="About" icon="info" />
      <SideMenuEntry label="Logout" icon="exit" />
    </SideMenu>
  </div>
</template>

<style scoped>
#dashboard-page {
  height: 100vh;
}

main {
  position: absolute;
  right: 0;
  width: calc(100% - v-bind("sideMenuOpen && sideMenuPinned ? `${sideMenuWidth}` : '0px'"));
  height: 100%;
  background-color: v-bind("theme.colBg1");
}

#side-menu {
  border-right: v-bind("!sideMenuOpen || menusExpanded ? 'none' : `2px solid ${theme.colFg1}`");
}

#user-menu {
  border-left: v-bind("!userMenuOpen || menusExpanded ? 'none' : `2px solid ${theme.colFg1}`");
  border-bottom: 2px solid v-bind("theme.colFg1");
}
</style>
