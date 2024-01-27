<script setup>
  import { useAppStore } from "@/storages/useAppStore";
  const appStore = useAppStore();
  const { toggleDarkMode } = appStore;

  import AppLogo from "./AppLogo.vue";
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
    <AppLogo id="app-logo" />
    <form id="login-form">
      <TextField placeholder="Username" icon="Person" />
      <TextField placeholder="Password" icon="Key" password invalid />
      <ClickButton>Login</ClickButton>
    </form>
  </div>
</template>

<style scoped>

#login-page {
  height: 100vh;
  text-align: center;
  background: linear-gradient(90deg, rgba(0,82,198,1) 0%, rgba(0,212,255,1) 100%);
}

#app-logo {
  height: 3.5em;
}

#login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 500px;
  margin: auto;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 5px;
}
</style>
