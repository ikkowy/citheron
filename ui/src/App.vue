<script setup>
import { ref, computed } from 'vue';

import { theme } from "./theme.js";

import SideMenuButton from "./components/SideMenuButton.vue";
import HeaderButton from "./components/HeaderButton.vue";

const sideMenuOpen = ref(false);

const appWidth = ref(window.innerWidth);
const appHeight = ref(window.innerHeight);

window.addEventListener("resize", () => {
  appWidth.value = window.innerWidth;
  appHeight.value = window.innerHeight;
});

const sideMenuWidth = 300;
const sideMenuExpandWidth = 500;

const sideMenuExpanded = computed(() => {
  return sideMenuOpen.value && appWidth.value <= sideMenuExpandWidth;
});

const sideMenuWidthPx = computed(() => {
  return sideMenuOpen.value ? `${sideMenuExpanded.value ? appWidth.value : sideMenuWidth}px` : "0px";
});

const mainDisplay = computed(() => {
  return sideMenuExpanded.value ? "none" : "inline-block";
});

const headerHeight = 40;
const headerHeightPx = `${headerHeight}px`;

const sideMenuHeightPx = computed(() => {
  return `${appHeight.value - headerHeight}px`;
});
</script>

<template>
  <header>
    <HeaderButton v-bind:icon="sideMenuOpen ? 'MenuOpen' : 'Menu'" v-on:click="sideMenuOpen = !sideMenuOpen" />
    <HeaderButton icon="AccountCircle" float="right" />
    <HeaderButton icon="Notifications" float="right" />
  </header>

  <main v-on:click="sideMenuOpen = false">
  </main>

  <aside>
    <SideMenuButton text="foo" />
    <SideMenuButton text="bar" />
    <SideMenuButton text="baz" />
  </aside>
</template>

<style>
body {
  margin: 0;
}

#app {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  width: 100%;
  height: v-bind(headerHeightPx);
  background-color: v-bind("theme.headerBackgroundColor");
}

aside {
  position: absolute;
  box-sizing: border-box;
  overflow: hidden;
  top: v-bind(headerHeightPx);
  width: v-bind(sideMenuWidthPx);
  height: v-bind(sideMenuHeightPx);
  background-color: v-bind("theme.sideMenuBackgroundColor");
  transition: width 500ms;
}

main {
  display: v-bind(mainDisplay);
  flex: 1;
}
</style>
