<script setup>
import { defineProps } from "vue";

import IconAccountCircle from "./icons/IconAccountCircle.vue";
import IconMenu from "./icons/IconMenu.vue";
import IconMenuOpen from "./icons/IconMenuOpen";
import IconNotifications from "./icons/IconNotifications.vue";

const props = defineProps(["name"]);
</script>

<template>
  <IconAccountCircle class="icon" v-if="props.name === 'AccountCircle'" />
  <IconMenu class="icon" v-else-if="props.name === 'Menu'" />
  <IconMenuOpen class="icon" v-else-if="props.name === 'MenuOpen'" />
  <IconNotifications class="icon" v-else-if="props.name === 'Notifications'" />
</template>

<style scoped>
</style>
