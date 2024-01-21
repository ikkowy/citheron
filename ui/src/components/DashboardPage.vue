<script setup>
import { ref, computed, watch } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme, toggleDarkMode, setDarkMode } = appStore;

import HeaderButton from "./HeaderButton.vue";
import SideMenu from "./SideMenu.vue";
import SideMenuEntry from "./SideMenuEntry.vue";

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
</script>

<template>
  <div id="dashboard-page">
    <header>
      <HeaderButton v-bind:icon="sideMenuOpen ? 'MenuOpen' : 'Menu'" v-on:click="sideMenuOpen = !sideMenuOpen" v-bind:active="sideMenuOpen" />
      <HeaderButton icon="AccountCircle" float="right" v-on:click="userMenuOpen = !userMenuOpen" v-bind:active="userMenuOpen" />
      <HeaderButton icon="Notifications" float="right" counter="42" />
      <HeaderButton v-bind:icon="appStore.darkModeEnabled ? 'DarkMode' : 'LightMode'" v-on:click="toggleDarkMode()" float="right" />
    </header>

    <main v-on:click="sideMenuOpen = false; userMenuOpen = false">
    </main>

    <SideMenu v-bind:width="sideMenuWidth" v-bind:height="`${appHeight - headerHeight}px`" v-bind:top="`${headerHeight}px`" entrydash="left" v-bind:open="sideMenuOpen">
      <SideMenuEntry label="Notes" icon="Book" />
      <SideMenuEntry label="Tasks" icon="Task" />
      <SideMenuEntry label="Vault" icon="Vault" />
      <SideMenuEntry label="Settings" icon="Settings" />
    </SideMenu>

    <SideMenu v-bind:width="userMenuWidth" v-bind:height="userMenuHeight" position="right" entryDash="false" v-bind:top="`${headerHeight}px`" v-bind:open="userMenuOpen">
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
