<script setup>
import { defineProps, ref, computed } from "vue";
import IconElement from "./IconElement.vue";

const props = defineProps({
  placeholder: String,
  icon: String,
  password: Boolean,
  invalid: Boolean
});

const showPassword = ref(false);
const focus = ref(false);

const border = computed(() => {
  if (focus.value || props.invalid) return "1px solid #ffffff";
  return "1px solid #d0d0d0";
});

const outline = computed(() => {
  if (props.invalid) return "2px solid hsla(5, 80%, 50%, 1)";
  return focus.value ? "2px solid #202020" : "none";
});

const iconColor = computed(() => {
  return props.invalid ? "hsla(5, 80%, 50%, 1)" : "#202020";
});

const textColor = computed(() => {
  return props.invalid ? "hsla(5, 80%, 50%, 1)" : "#202020";
});
</script>

<template>
  <div class="text-field">
    <IconElement v-if="props.icon" v-bind:fill="iconColor" v-bind:name="props.icon" />
    <input class="text-field-input" v-bind:type="props.password && !showPassword ? 'password' : 'text'" v-bind:placeholder="props.placeholder" v-on:focusin="focus = true" v-on:focusout="focus = false">
    <IconElement class="text-field-show-password" v-bind:fill="iconColor" v-bind:name="showPassword ? 'VisibilityOff' : 'Visibility'" v-if="props.password" v-on:click="showPassword = !showPassword" />
  </div>
</template>

<style scoped>
.text-field {
  display: flex;
  flex-direction: row;
  gap: 10px;
  border: v-bind(border);
  outline: v-bind(outline);
  padding: 12px 15px;
  border-radius: 5px;
}

.text-field-input {
  width: 100%;
  margin: 0;
  padding: 0;
  border: none;
  outline: none;
  font-size: 16px;
  color: v-bind(textColor);
}

.text-field-input::placeholder {
  opacity: 1;
}

.text-field-show-password:hover {
  cursor: pointer;
}
</style>
