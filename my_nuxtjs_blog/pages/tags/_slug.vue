<template>
    <div>
        <Header :name=title />
        <div class="container">
            <p class="my-3">Другие теги:
                <nuxt-link :to="`/tags/${tag.name}`" class="badge badge-success mr-1" v-for="tag in tags"
                    :key="name">#{{ tag.name }} </nuxt-link>
            </p>
            <div class="row">
                <div v-for="position in positions" :key="position.slug" class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h4 class="card-title">{{ position.name }}</h4>
                            <div v-html="position.sostav" class="truncate"></div>
                            <div class="mb-2">
                                <span v-for="tag in position.tags">
                                    <nuxt-link :to="`/tags/${tag}`" class="badge bg-warning mr-2 catg-tag">{{ tag
                                        }}</nuxt-link>
                                </span>
                            </div>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <nuxt-link :to="`/positions/${position.slug}`"
                                        class="btn btn-sm btn-outline-secondary">Подробнее</nuxt-link>
                                </div>
                                <div>{{ position.price }} р</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Header from "@/components/Header";

export default {
    components: { Header },
    layout: "post_detail",
    async asyncData({ params }) {
        const { data } = await axios.get(`http://127.0.0.1:8000/api/tags/${params.slug}`);
        const tags = await axios.get(`http://127.0.0.1:8000/api/tags/`);
        return {
            positions: data.results,
            title: `#${params.slug}`,
            tags: tags.data,
        }
    },
}
</script>