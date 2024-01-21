<script setup>
import { ref } from "vue";

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
      <HeaderButton v-bind:icon="sideMenuOpen ? 'MenuOpen' : 'Menu'" v-on:click="sideMenuOpen = !sideMenuOpen" />
      <HeaderButton icon="AccountCircle" float="right" />
      <HeaderButton icon="Notifications" float="right" counter="42" />
      <HeaderButton v-bind:icon="appStore.darkModeEnabled ? 'DarkMode' : 'LightMode'" v-on:click="toggleDarkMode()" float="right" />
    </header>

    <main v-on:click="sideMenuOpen = false">
    </main>

    <SideMenu width="300px" v-bind:height="`${appHeight - headerHeight}px`" v-bind:top="`${headerHeight}px`" v-bind:open="sideMenuOpen">
      <SideMenuEntry label="Notes" icon="Book" />
      <SideMenuEntry label="Tasks" icon="Task" />
      <SideMenuEntry label="Vault" icon="Vault" />
      <SideMenuEntry label="Settings" icon="Settings" />
      <SideMenuEntry label="Help" icon="Help" />
      <SideMenuEntry label="About" icon="Info" />
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
