<script setup>
import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;
</script>

<template>
  <div class="dashboard-panel">
    <slot />
  </div>
</template>

<style scoped>
.dashboard-panel {
  height: 100%;
  padding: 10px;
  color: v-bind("theme.colFg1");
}
</style>
