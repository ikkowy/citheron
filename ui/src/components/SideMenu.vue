<script setup>
import { defineProps } from "vue";

// import { theme } from "../theme.js";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  width: String,
  height: String,
  top: String,
  open: {
    type: Boolean,
    default: false
  },
  expanded: {
    type: Boolean,
    default: false
  }
});
</script>

<template>
  <aside id="side-menu">
    <slot />
  </aside>
</template>

<style scoped>
#side-menu {
  position: absolute;
  box-sizing: border-box;
  overflow: hidden;
  top: v-bind("props.top");
  width: v-bind("props.open ? props.width : '0px'");
  height: v-bind("props.height");
  background-color: v-bind("theme.sideMenuBackgroundColor");
  transition: width 500ms;
}
</style>
