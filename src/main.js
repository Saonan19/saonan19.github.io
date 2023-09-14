import { createApp } from 'vue'
import App from './App.vue'
import VueAwesomePaginate from "vue-awesome-paginate";
import "vue-awesome-paginate/dist/style.css";

// createApp(App).mount('#app')
// import the package

// import the necessary css file

// Register the package
createApp(App).use(VueAwesomePaginate).mount("#app");