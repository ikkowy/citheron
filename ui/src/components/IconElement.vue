<script setup>
import { defineProps } from "vue";

import IconAccountCircle from "./icons/IconAccountCircle.vue";
import IconDarkMode from "./icons/IconDarkMode.vue";
import IconLightMode from "./icons/IconLightMode.vue";
import IconMenu from "./icons/IconMenu.vue";
import IconMenuOpen from "./icons/IconMenuOpen";
import IconNotifications from "./icons/IconNotifications.vue";
import IconPin from "./icons/IconPin.vue";
import IconPinSlash from "./icons/IconPinSlash.vue";

const props = defineProps(["name"]);
</script>

<template>
  <IconAccountCircle class="icon" v-if="props.name === 'AccountCircle'" />
  <IconDarkMode class="icon" v-else-if="props.name === 'DarkMode'" />
  <IconLightMode class="icon" v-else-if="props.name === 'LightMode'" />
  <IconMenu class="icon" v-else-if="props.name === 'Menu'" />
  <IconMenuOpen class="icon" v-else-if="props.name === 'MenuOpen'" />
  <IconNotifications class="icon" v-else-if="props.name === 'Notifications'" />
  <IconPin class="icon" v-else-if="props.name === 'Pin'" />
  <IconPinSlash class="icon" v-else-if="props.name === 'PinSlash'" />
</template>

<style scoped>
</style>
