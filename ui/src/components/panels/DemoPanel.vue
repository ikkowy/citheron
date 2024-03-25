<script setup>
import DashboardPanel from '../DashboardPanel.vue';
import IwyButton from '../iwy/IwyButton.vue';
import IwyTextField from '../iwy/IwyTextField.vue';

import { useAppStore } from "@/storages/useAppStore";
const appStore = useAppStore();
const { theme } = appStore;
</script>

<template>
  <DashboardPanel>
    <div style="display: flex; flex-direction: column; gap: 10px">
      <IwyTextField />
      <IwyTextField placeholder="Placeholder" />
      <IwyTextField icon="search" button="Search" />
      <IwyTextField icon="pencil" />
      <IwyTextField icon="key" button="Verify" password invalid />

      <div style="display: flex; gap: 10px">
        <IwyButton label="Button" />
        <IwyButton label="Book now!" icon="book" />
      </div>

      <div style="display: flex; gap: 10px">
        <div :style="`display: inline-block; width: 100px; height: 100px; background-color: ${theme.colRed}`"></div>
        <div :style="`display: inline-block; width: 100px; height: 100px; background-color: ${theme.colBlue}`"></div>
        <div :style="`display: inline-block; width: 100px; height: 100px; background-color: ${theme.colGreen}`"></div>
        <div :style="`display: inline-block; width: 100px; height: 100px; background-color: ${theme.colYellow}`"></div>
      </div>
    </div>
  </DashboardPanel>
</template>

<style scoped>
</style>
