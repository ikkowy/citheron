<script setup>
import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;
</script>

<template>
  <header class="navbar">
    <slot />
  </header>
</template>

<style scoped>
.navbar {
  width: 100%;
  height: 40px;
  background-color: v-bind("theme.colBg2");
}
</style>
