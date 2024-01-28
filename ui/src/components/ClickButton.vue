<script setup>
import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;
</script>

<template>
  <button class="click-button">
    <slot />
  </button>
</template>

<style scoped>
.click-button {
  box-sizing: border-box;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 7px 15px;
  border-radius: 5px;
  font-weight: bold;
  background-color: v-bind("theme.colFg1");
  color: v-bind("theme.colBg1");
  transition: background-color 200ms;
}

.click-button:hover {
  background-color: v-bind("theme.colFg3");
  cursor: pointer;
}
</style>
