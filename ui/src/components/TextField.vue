<script setup>
import { defineProps } from "vue";

const props = defineProps({
  placeholder: String,
  password: Boolean
});
</script>

<template>
  <input class="text-field" v-bind:type="props.password ? 'password' : 'text'" v-bind:placeholder="props.placeholder">
</template>

<style scoped>
.text-field {
  box-sizing: border-box;
  border: 1px solid #d0d0d0;
  outline: none;
  font-size: 16px;
  padding: 12px 15px;
  border-radius: 5px;
}

.text-field:focus {
  border: 1px solid #d0d0d0;
  outline: 2px solid hsla(215, 80%, 50%, 1);
}
</style>
