<template>
    <div class="container-fluid home-slider">
        <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active" style="background-color: #343a40!important">
                    <div class="carousel-caption d-none d-md-block">
                        <form class="my-2 my-lg-0">
                            <input name="q" type="text" class="form-control" placeholder="Поиск" aria-label="Поиск"
                                v-model="q">
                            <button class="btn btn-outline-success mt-3"
                                @click.stop.prevent="searchPositions()">Поиск</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            q: '',
            positions: ''
        }
    },
    methods: {
        async searchPositions() {
            this.positions = await axios.get(`http://localhost:8000/api/positions/?search=${this.q}`);
            this.$router.push("/search?q=" + this.q);
            this.$emit('searchPositions', this.positions.data);
        },
    }
}
</script>