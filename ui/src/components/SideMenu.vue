<script setup>
import { computed, provide } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  open: {
    type: Boolean,
    default: true
  }
});
</script>

<template>
  <aside class="side-menu">
    <slot />
  </aside>
</template>

<style scoped>
.side-menu {
  display: v-bind("props.open ? 'initial' : 'none'");
  box-sizing: border-box;
  background-color: v-bind("theme.colBg");
}
</style>
