<script setup>
import { defineProps } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;

import IconElement from "./IconElement.vue";

const props = defineProps({
  caption: String,
  buttonLeftEnabled: {
    type: Boolean,
    default: true
  },
  buttonRightEnabled: {
    type: Boolean,
    default: true
  },
  buttonLeftActive: {
    type: Boolean,
    default: true
  },
  buttonRightActive: {
    type: Boolean,
    default: true
  },
  buttonLeftIcon: String,
  buttonRightIcon: String,
  buttonLeftAction: {
    type: Function,
    default: () => { }
  },
  buttonRightAction: {
    type: Function,
    default: () => { }
  }
});
</script>

<template>
  <div class="side-menu-banner" v-if="props.caption || props.buttonLeftEnabled || props.buttonRightEnabled">
    <a v-if="props.buttonLeftEnabled && props.buttonLeftIcon" v-on:click="props.buttonLeftAction()"
      v-bind:class="{ 'side-menu-banner-button': true, 'left': true, 'active': props.buttonLeftActive }">
      <IconElement v-bind:name="props.buttonLeftIcon" v-bind:fill="theme.sideMenuForegroundColor" />
    </a>
    <a v-if="props.buttonRightEnabled && props.buttonRightIcon" v-on:click="props.buttonRightAction()"
      v-bind:class="{ 'side-menu-banner-button': true, 'right': true, 'active': props.buttonRightActive }">
      <IconElement v-bind:name="props.buttonRightIcon" v-bind:fill="theme.sideMenuForegroundColor" />
    </a>
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

.side-menu-banner-button:not(.active) {
  opacity: 0.5;
}

.side-menu-banner-button.active:hover {
  background-color: v-bind("theme.sideMenuHoverBackgroundColor");
}

.side-menu-banner-button.left {
  left: 0;
}

.side-menu-banner-button.right {
  right: 0;
}
</style>
