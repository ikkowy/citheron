<script setup>
import IconAccountCircle from "./components/icons/IconAccountCircle.vue";
import IconMenu from "./components/icons/IconMenu.vue";
import IconMenuOpen from "./components/icons/IconMenuOpen";
import IconNotifications from "./components/icons/IconNotifications.vue";
import SideMenuButton from "./components/SideMenuButton.vue";
</script>

<template>
  <header>
    <a class="header-button" style="float: left" v-on:click="sideMenuOpen = !sideMenuOpen">
      <IconMenu v-if="!sideMenuOpen" />
      <IconMenuOpen v-else />
    </a>

    <a class="header-button" style="float: right">
      <IconAccountCircle />
    </a>

    <a class="header-button" style="float: right">
      <IconNotifications />
    </a>
  </header>

  <main v-on:click="sideMenuOpen = false">
  </main>

  <aside>
    <SideMenuButton text="foo" />
    <SideMenuButton text="bar" />
    <SideMenuButton text="baz" />
  </aside>
</template>

<script>
import { ref, computed } from 'vue';

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

export default {
  name: "App"
};
</script>

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
  background-color: #1a1a1a;
}

.header-button {
  display: flex;
  align-items: center;
  height: 100%;
  aspect-ratio: 1 / 1;
}

.header-button:hover {
  cursor: pointer;
  background-color: #262626;
}

.header-button svg {
  display: block;
  margin: auto;
  width: 70%;
  fill: #d9d9d9;
}

aside {
  position: absolute;
  box-sizing: border-box;
  overflow: hidden;
  top: v-bind('headerHeightPx');
  width: v-bind('sideMenuWidthPx');
  height: v-bind('sideMenuHeightPx');
  background-color: #1a1a1a;
  transition: width 500ms;
}

main {
  display: v-bind('mainDisplay');
  flex: 1;
}
</style>
