<script setup>
import { defineProps } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

import IconElement from "./IconElement.vue";

const props = defineProps({
  caption: String,
  buttonLeftIcon: String,
  buttonRightIcon: String,
  buttonLeftAction: Function
});
</script>

<template>
  <div class="side-menu-banner">
    <a v-if="props.buttonLeftIcon" v-on:click="props.buttonLeftAction()" class="side-menu-banner-button side-menu-banner-button-back"> <IconElement v-bind:name="props.buttonLeftIcon" v-bind:fill="theme.sideMenuForegroundColor" /></a>
    <a v-if="props.buttonRightIcon" class="side-menu-banner-button side-menu-banner-button-pin"> <IconElement v-bind:name="props.buttonRightIcon" v-bind:fill="theme.sideMenuForegroundColor" /></a>
    <span v-if="props.caption">{{ props.caption }}</span>
  </div>
</template>

<style scoped>
.side-menu-banner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40px;
  font-weight: bold;
  color: v-bind("theme.sideMenuForegroundColor");
  user-select: none;
}

.side-menu-banner span {
  padding: 3px 8px;
  background-color: v-bind("theme.sideMenuForegroundColor");
  color: v-bind("theme.sideMenuBackgroundColor");
  border-radius: 7px;
}

.side-menu-banner-button {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  cursor: pointer;
}

.side-menu-banner-button:hover {
  background-color: v-bind("theme.sideMenuHoverBackgroundColor");
}

.side-menu-banner-button-back {
  left: 0;
}

.side-menu-banner-button-pin {
  right: 0;
}
</style>
