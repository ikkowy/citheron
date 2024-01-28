<script setup>
import { defineProps } from "vue";

import IconAccountCircle from "./icons/IconAccountCircle.vue";
import IconBack from "./icons/IconBack.vue";
import IconBook from "./icons/IconBook.vue";
import IconDarkMode from "./icons/IconDarkMode.vue";
import IconGroup from "./icons/IconGroup.vue";
import IconHelp from "./icons/IconHelp.vue";
import IconInfo from "./icons/IconInfo.vue";
import IconKey from "./icons/IconKey.vue";
import IconLightMode from "./icons/IconLightMode.vue";
import IconLogout from "./icons/IconLogout.vue";
import IconMenu from "./icons/IconMenu.vue";
import IconMenuOpen from "./icons/IconMenuOpen";
import IconNotifications from "./icons/IconNotifications.vue";
import IconPerson from "./icons/IconPerson.vue";
import IconPin from "./icons/IconPin.vue";
import IconPinSlash from "./icons/IconPinSlash.vue";
import IconSearch from "./icons/IconSearch.vue";
import IconServer from "./icons/IconServer.vue";
import IconSettings from "./icons/IconSettings.vue";
import IconTask from "./icons/IconTask.vue";
import IconVault from "./icons/IconVault.vue";
import IconVisibility from "./icons/IconVisibility.vue";
import IconVisibilityOff from "./icons/IconVisibilityOff.vue";

const props = defineProps(["name"]);
</script>

<template>
  <IconAccountCircle v-if="props.name === 'AccountCircle'" />
  <IconBack v-else-if="props.name === 'Back'" />
  <IconBook v-else-if="props.name === 'Book'" />
  <IconDarkMode v-else-if="props.name === 'DarkMode'" />
  <IconGroup v-else-if="props.name === 'Group'" />
  <IconHelp v-else-if="props.name === 'Help'" />
  <IconInfo v-else-if="props.name === 'Info'" />
  <IconKey v-else-if="props.name === 'Key'" />
  <IconLightMode v-else-if="props.name === 'LightMode'" />
  <IconLogout v-else-if="props.name === 'Logout'" />
  <IconMenu v-else-if="props.name === 'Menu'" />
  <IconMenuOpen v-else-if="props.name === 'MenuOpen'" />
  <IconNotifications v-else-if="props.name === 'Notifications'" />
  <IconPerson v-else-if="props.name === 'Person'" />
  <IconPin v-else-if="props.name === 'Pin'" />
  <IconPinSlash v-else-if="props.name === 'PinSlash'" />
  <IconSearch v-else-if="props.name === 'Search'" />
  <IconServer v-else-if="props.name === 'Server'" />
  <IconSettings v-else-if="props.name === 'Settings'" />
  <IconTask v-else-if="props.name === 'Task'" />
  <IconVault v-else-if="props.name === 'Vault'" />
  <IconVisibility v-else-if="props.name === 'Visibility'" />
  <IconVisibilityOff v-else-if="props.name === 'VisibilityOff'" />
</template>

<style scoped>
</style>
