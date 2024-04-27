<template>
  <div>
    <SearchHeader @searchpositions="positions = $event" />
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <nav aria-label="breadcrumb" class="mt-4">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><nuxt-link to="/">Главная</nuxt-link></li>
              <li class="breadcrumb-item active" aria-current="page">Поиск</li>
            </ol>
          </nav>
          <p class="lead">Найдено записей: {{ positions.count }}</p>
          <div v-for="position in positions.results" :key="position.id">
            <nuxt-link :to="`/positions/${position.slug}`">
              <h2>{{ position.name }}</h2>
            </nuxt-link>
            <p v-html="position.sostav"></p>
            <hr>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchHeader from "@/components/SearchHeader";
import axios from "axios";
export default {
  components: { SearchHeader },
  layout: "position_detail",
  watchQuery: ['q'],
  data() {
    return {
      positions: ''
    }
  },
  async asyncData({ route }) {
    const { data } = await axios.get(`http://localhost:8000/api/positions/?q=${route.query.q}`);
    return {
      positions: data,
    }
  },
}
</script>

<style scoped></style>