<script setup>
import { defineProps } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

import IconElement from "./IconElement.vue";

const props = defineProps({
  label: String,
  icon: String
});
</script>

<template>
  <div class="side-menu-button">
    <IconElement v-if="props.icon" v-bind:name="props.icon" v-bind:fill="theme.SideMenuEntryForegroundColor" />
    <span>{{ props.label }}</span>
  </div>
</template>

<style scoped>
.side-menu-button {
    display: flex;
    align-items: center;
    width: 100%;
    height: 40px;
    padding-left: 20px;
    background-color: v-bind("theme.SideMenuEntryBackgroundColor");
    color: v-bind("theme.SideMenuEntryForegroundColor");
    user-select: none;
}

.side-menu-button:hover {
    cursor: pointer;
    background-color: v-bind("theme.SideMenuEntryHoverBackgroundColor");
    padding-left: 15px; 
    border-left: 5px solid v-bind("theme.SideMenuEntryForegroundColor");
}

.side-menu-button span {
    margin-left: 15px;
    font-weight: bold;
}
</style>
