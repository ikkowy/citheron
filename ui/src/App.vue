<script setup>
import IconAccountCircle from "./components/icons/IconAccountCircle.vue";
import IconMenu from "./components/icons/IconMenu.vue";
import IconMenuOpen from "./components/icons/IconMenuOpen";
import IconNotifications from "./components/icons/IconNotifications.vue";
import IconPin from "./components/icons/IconPin.vue";
import IconPinSlash from "./components/icons/IconPinSlash.vue";
</script>

<template>

  <header>

    <a class="header-button" style="float: left" v-on:click="sideMenuOpen = !sideMenuOpen">
      <IconMenu v-if="!sideMenuOpen" />
      <IconMenuOpen v-else />
    </a>

    <a class="header-button" style="float: left" v-if="sideMenuOpen" v-on:click="sideMenuPinned = !sideMenuPinned">
      <IconPin v-if="!sideMenuPinned" />
      <IconPinSlash v-else />
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

  <main v-on:click="sideMenuOpen = false">
  </main>

</template>

<script>
import { ref, computed } from 'vue';

const sideMenuOpen = ref(false);
const sideMenuPinned = ref(false);
const sideMenuWidth = ref("300px");

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
  height: 40px;
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
  width: v-bind('sideMenuWidth');
  height: calc(100vh - 40px);
  background-color: #1a1a1a;
  border-top: 1px solid #262626;
}

main {
  position: absolute;
  top: 40px;
  right: 0;
  width: calc(100vw - v-bind('sideMenuWidth'));
  height: calc(100vh - 40px);
  background-color: green;
}
</style>
