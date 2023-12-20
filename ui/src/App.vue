<script setup>
import IconAccountCircle from "./components/icons/IconAccountCircle.vue";
import IconMenu from "./components/icons/IconMenu.vue";
import IconMenuOpen from "./components/icons/IconMenuOpen";
import IconNotifications from "./components/icons/IconNotifications.vue";
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

  <aside>
  </aside>

  <main>
  </main>

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

const sideMenuMaxWidth = 500;

const sideMenuExpanded = computed(() => {
  return sideMenuOpen.value && appWidth.value <= sideMenuMaxWidth;
});

const sideMenuWidthPx = computed(() => {
  return sideMenuOpen.value ? `${sideMenuExpanded.value ? appWidth.value : sideMenuMaxWidth}px` : "0px";
});

const mainDisplay = computed(() => {
  return sideMenuExpanded.value ? "none" : "inline-block";
});

const headerHeight = 40;
const headerHeightPx = `${headerHeight}px`;

const sideMenuHeightPx = computed(() => {
  return `${appHeight.value - headerHeight}px`;
});

const sideMenuVisibility = computed(() => {
  return sideMenuOpen.value ? "visible" : "hidden";
});

export default {
  name: 'App'
};
</script>

<style>
body {
  margin: 0;
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
  box-sizing: border-box;
  visibility: v-bind('sideMenuVisibility');
  width: v-bind('sideMenuWidthPx');
  height: v-bind('sideMenuHeightPx');
  background-color: #1a1a1a;
  border-top: 1px solid #262626;
}

main {
  display: v-bind('mainDisplay');
  position: absolute;
  overflow: scroll;
  top: 40px;
  right: 0;
  width: calc(100vw - v-bind('sideMenuWidthPx'));
  height: calc(100vh - v-bind('headerHeightPx'));
}
</style>
