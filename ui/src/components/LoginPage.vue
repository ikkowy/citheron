<script setup>
  import { useAppStore } from "@/storages/useAppStore";
  const appStore = useAppStore();
  const { theme, toggleDarkMode } = appStore;

  import TextField from "./TextField.vue";
  import ClickButton from "./ClickButton.vue";
  import NavBar from "./NavBar.vue";
  import NavBarButton from "./NavBarButton.vue";
</script>

<template>
  <div id="login-page">
    <NavBar>
      <NavBarButton
      v-bind:icon="appStore.darkModeEnabled ? 'DarkMode' : 'LightMode'"
      v-on:click="toggleDarkMode()"
      float="right" />
    </NavBar>
    <form id="login-form">
      <TextField placeholder="Username" icon="Person" width="100%"/>
      <TextField placeholder="Password" icon="Key" password />
      <ClickButton inverted>Login</ClickButton>
    </form>
  </div>
</template>

<style scoped>
#login-page {
  height: 100vh;
  text-align: center;
  background-color: v-bind("theme.colBg1");
}

#login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 500px;
  margin-top: 10vh;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
  border: 2px solid v-bind("theme.colFg1");
  border-radius: 5px;
}
</style>
