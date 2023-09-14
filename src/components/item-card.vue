<template>
  <div class="grid-container" ref="top">
  
    <div v-for="service in services" :key="service['name']">
      <card :title="service['name']" :description="service['description']" :src="service['image']" :website="service['website']" ref="card"/>
    </div>
  </div>
  <paginate :page-count="pageCount" :page-range="pageRange" :margin-pages="marginPage" :click-handler="clickCallback"
  :prev-text="'Prev'" :next-text="'Next'" :container-class="'pagination'" :page-class="'page-item'" />
</template>

<script>
import Paginate from 'vuejs-paginate-next';
import Card from "./card-item.vue";
import services from "../assets/services.json";
export default {
  components: {
    paginate: Paginate,
    card: Card,
  },
  data() {
    return {
      per_page: 12,
      services: services.slice(0,12),
      pageCount: Math.ceil(services.length/12),
      pageRange: 3,
      marginPage: 2,
    }
  },
  methods: {
    clickCallback(pageNum) {
      var len = pageNum * this.per_page >= services.length ? services.length : pageNum * this.per_page;
      this.services = services.slice(len-this.per_page, len);
      this.$refs.top.scrollIntoView()
    }
  },
};
</script>

<style lang="css">
/* Adopt bootstrap pagination stylesheet. */
@import "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css";

/* Write your own CSS for pagination */
.pagination {
  justify-content: center;
  margin-top: 50px ;
}

.grid-container {
  display: grid;
  column-gap: 10px;
  grid-template-columns: auto auto auto;
  padding: 10px;
  justify-items: center;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
@media (min-width: 300px) {
  .grid-container {
    column-gap: 0px;
    padding: 0px;
      column-count: 2;
      column-gap: 0.5rem;
      orphans: 2;
      widows: 2 !important;
  }
}
</style>