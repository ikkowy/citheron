<script setup>
import { defineProps } from "vue";

// import { theme } from "../theme.js";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

const props = defineProps({
  text: String
});
</script>

<template>
  <div class="side-menu-button">
    <span>{{ props.text }}</span>
  </div>
</template>

<style scoped>
.side-menu-button {
    display: flex;
    align-items: center;
    width: 100%;
    height: 40px;
    background-color: v-bind("theme.sideMenuButtonBackgroundColor");
    color: v-bind("theme.sideMenuButtonForegroundColor");
    user-select: none;
}

.side-menu-button:hover {
    cursor: pointer;
    background-color: v-bind("theme.sideMenuButtonHoverBackgroundColor");
}

.side-menu-button span {
    margin-left: 30px;
}
</style>
