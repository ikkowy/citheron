<script setup>
import { ref, computed, onMounted } from "vue";

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme, toggleDarkMode } = appStore;

import NavBar from "./NavBar.vue";
import NavBarButton from "./NavBarButton.vue";
import SideMenu from "./SideMenu.vue";
import SideMenuEntry from "./SideMenuEntry.vue";
import SideMenuSection from "./SideMenuSection.vue";
import SideMenuBanner from "./SideMenuBanner.vue";

// import DemoPanel from "./panels/DemoPanel.vue";
import UserPanel from "./panels/UserPanel.vue";

const appWidth = ref(window.innerWidth);
const appHeight = ref(window.innerHeight);

window.addEventListener("resize", () => {
  appWidth.value = document.getElementById("app").offsetWidth;
  appHeight.value = document.getElementById("app").offsetHeight;
});

const sideMenuOpen = ref(false);
const userMenuOpen = ref(false);

const sideMenuPinned = ref(false);

const menuExpandLimit = 600;

const menusExpanded = computed(() => {
  return appWidth.value < menuExpandLimit;
});

function closeMenus() {
  if (!sideMenuPinned.value)
    sideMenuOpen.value = false;
  userMenuOpen.value = false;
}

const sideMenuBannerCaption = ref("");
const sideMenuPreviousSection = ref("");

function changeSideMenuSection(name) {
  const sideMenu = document.getElementById("side-menu");
  const sideMenuSections = sideMenu.getElementsByClassName("side-menu-section");
  Array.prototype.forEach.call(sideMenuSections, (element) => {
    element.style.display = "none";
    if (element.getAttribute("data-side-menu-section-name") == name) {
      element.style.display = "initial";
      sideMenuBannerCaption.value = element.getAttribute("data-side-menu-section-caption");
      sideMenuPreviousSection.value = element.getAttribute("data-side-menu-section-back");
    }
  });
}

function previousSideMenuSection() {
  const prev = sideMenuPreviousSection.value;
  if (prev) changeSideMenuSection(prev);
}

onMounted(() => {
  changeSideMenuSection("apps");
});
</script>

<template>
  <div style="display: flex; flex-direction: column; height: 100vh">
    <NavBar style="flex-grow: 0; flex-shrink: 0">
      <NavBarButton
          :icon="sideMenuOpen ? 'menu-open' : 'menu'"
          @click="sideMenuOpen = !sideMenuOpen"
          :active="sideMenuOpen" />
      <NavBarButton
          icon="user-circle"
          float="right"
          @click="userMenuOpen = !userMenuOpen"
          :active="userMenuOpen" />
      <NavBarButton icon="bell" float="right" counter="42" />
      <NavBarButton
          :icon="appStore.darkModeEnabled ? 'dark' : 'light'"
          @click="toggleDarkMode()"
          float="right" />
    </NavBar>
    <div style="display: flex; flex-direction: row; flex: 1">
      <SideMenu id="side-menu" :open="sideMenuOpen">
        <SideMenuBanner
            :caption="sideMenuBannerCaption"
            :button-left-active="sideMenuPreviousSection"
            :button-right-active="!menusExpanded"
            button-left-icon="chevron-left"
            :button-right-icon="sideMenuPinned ? 'pin-off' : 'pin'"
            :button-left-action="previousSideMenuSection"
            :button-right-action="() => { if (!menusExpanded) { sideMenuPinned = !sideMenuPinned } }" />
        <SideMenuSection name="apps">
          <SideMenuEntry label="Notes" icon="book" />
          <SideMenuEntry label="Tasks" icon="task" />
          <SideMenuEntry label="Vault" icon="vault" />
          <SideMenuEntry label="Administration" icon="server" @click="changeSideMenuSection('admin')" />
          <SideMenuEntry label="Settings" icon="gear" @click="changeSideMenuSection('settings')" />
        </SideMenuSection>
        <SideMenuSection name="admin" caption="Administration" back="apps">
          <SideMenuEntry label="Users" icon="user" />
          <SideMenuEntry label="Groups" icon="group" />
          <SideMenuEntry label="Authentication" icon="key" />
        </SideMenuSection>
        <SideMenuSection name="settings" caption="Settings" back="apps">
          <SideMenuEntry label="Security" icon="lock" />
        </SideMenuSection>
      </SideMenu>
      <SideMenu
          id="user-menu"
          :open="userMenuOpen">
        <SideMenuEntry label="Help" icon="help" />
        <SideMenuEntry label="About" icon="info" />
        <SideMenuEntry label="Logout" icon="exit" />
      </SideMenu>

      <main v-if="!(menusExpanded && sideMenuOpen)" @click="closeMenus()">
        <!-- <DemoPanel /> -->
        <UserPanel />
      </main>
    </div>
  </div>
</template>

<style scoped>
#side-menu {
  z-index: 1;
  position: v-bind("sideMenuPinned ? 'relative' : 'absolute'");
  border-right: v-bind("!sideMenuOpen || menusExpanded ? 'none' : `2px solid ${theme.colFg}`");
  width: v-bind("menusExpanded ? '100%' : '250px'");
  flex-grow: 0;
  flex-shrink: 0;
  height: 100%;
}

main {
  flex: 1;
  background-color: v-bind("theme.colBg");
}

#user-menu {
  position: absolute;
  z-index: 2;
  right: 0;
  width: v-bind("menusExpanded ? '100%' : 'initial'");
  height: v-bind("menusExpanded ? '100%' : 'initial'");
  border-left: v-bind("!userMenuOpen || menusExpanded ? 'none' : `2px solid ${theme.colFg}`");
  border-bottom: 2px solid v-bind("theme.colFg");
}
</style>
