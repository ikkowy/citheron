<script setup>
import { defineProps } from "vue";

import IconAccountCircle from "./icons/IconAccountCircle.vue";
import IconDarkMode from "./icons/IconDarkMode.vue";
import IconKey from "./icons/IconKey.vue";
import IconLightMode from "./icons/IconLightMode.vue";
import IconMenu from "./icons/IconMenu.vue";
import IconMenuOpen from "./icons/IconMenuOpen";
import IconNotifications from "./icons/IconNotifications.vue";
import IconPerson from "./icons/IconPerson.vue";
import IconPin from "./icons/IconPin.vue";
import IconPinSlash from "./icons/IconPinSlash.vue";
import IconVisibility from "./icons/IconVisibility.vue";
import IconVisibilityOff from "./icons/IconVisibilityOff.vue";

const props = defineProps(["name"]);
</script>

<template>
  <IconAccountCircle class="icon" v-if="props.name === 'AccountCircle'" />
  <IconDarkMode class="icon" v-else-if="props.name === 'DarkMode'" />
  <IconKey class="icon" v-else-if="props.name === 'Key'" />
  <IconLightMode class="icon" v-else-if="props.name === 'LightMode'" />
  <IconMenu class="icon" v-else-if="props.name === 'Menu'" />
  <IconMenuOpen class="icon" v-else-if="props.name === 'MenuOpen'" />
  <IconNotifications class="icon" v-else-if="props.name === 'Notifications'" />
  <IconPerson class="icon" v-else-if="props.name === 'Person'" />
  <IconPin class="icon" v-else-if="props.name === 'Pin'" />
  <IconPinSlash class="icon" v-else-if="props.name === 'PinSlash'" />
  <IconVisibility class="icon" v-else-if="props.name === 'Visibility'" />
  <IconVisibilityOff class="icon" v-else-if="props.name === 'VisibilityOff'" />
</template>

<style scoped>
</style>
