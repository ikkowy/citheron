<script setup>
import { ref } from "vue";

import { theme, darkModeEnabled } from "./theme.js";

import HeaderButton from "./components/HeaderButton.vue";
import SideMenu from "./components/SideMenu.vue";
import SideMenuButton from "./components/SideMenuButton.vue";

const appWidth = ref(window.innerWidth);
const appHeight = ref(window.innerHeight);

window.addEventListener("resize", () => {
  appWidth.value = document.getElementById("app").offsetWidth;
  appHeight.value = document.getElementById("app").offsetHeight;
});

const headerHeight = 40;

const sideMenuOpen = ref(false);

if (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) {
  darkModeEnabled.value = true;
}
</script>

<template>
  <header>
    <HeaderButton v-bind:icon="sideMenuOpen ? 'MenuOpen' : 'Menu'" v-on:click="sideMenuOpen = !sideMenuOpen" />
    <HeaderButton icon="AccountCircle" float="right" />
    <HeaderButton icon="Notifications" float="right" counter="42" />
    <HeaderButton v-bind:icon="darkModeEnabled ? 'DarkMode' : 'LightMode'" v-on:click="darkModeEnabled = !darkModeEnabled" float="right" />
  </header>

  <main v-on:click="sideMenuOpen = false">
  </main>

  <SideMenu width="300px" v-bind:height="`${appHeight - headerHeight}px`" v-bind:top="`${headerHeight}px`" v-bind:open="sideMenuOpen">
    <SideMenuButton text="foo" />
    <SideMenuButton text="bar" />
    <SideMenuButton text="baz" />
  </SideMenu>
</template>

<style>
#app {
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
  background-color: v-bind("theme.mainBackgroundColor.value");
}
</style>
