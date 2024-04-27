<template>
    <div>
        <Header :name=position.name />
        <div class="container">
            <div class="row">
                <div class="col-lg-8">
                    <nav aria-label="breadcrumb" class="mt-4">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><nuxt-link to="/">Главная</nuxt-link></li>
                            <li class="breadcrumb-item active" aria-current="page">{{ position.name }}</li>
                        </ol>
                    </nav>
                    <h1>{{ position.name }}</h1>
                    <hr>
                    <p v-html="position.sostav">
                    </p>
                    Цена:<div v-html="position.price" class="btn btn-sm m-1"></div>рублей
                    <div class="d-flex justify-content-end">
                        <span v-for="tag in position.tags">
                            <nuxt-link :to="`/tags/${tag}`" class="mr-1 badge badge-info">#{{ tag }}</nuxt-link>
                        </span>
                    </div>
                    <hr>
                    <Comments :comments="comments"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import position_detail from "@/layouts/position_detail";
import Header from "~/components/Header";
import Comments from "@/components/Comments";
export default {
    components: {
        Header,
        Comments
    },
    layout: "position_detail",
    async asyncData({ params }) {
        const position = await axios.get(`http://127.0.0.1:8000/api/positions/${params.slug}`);
        const tags = await axios.get(`http://127.0.0.1:8000/api/tags/`);
        const comments = await axios.get(`http://127.0.0.1:8000/api/comments/${params.slug}`);
        return {
            position: position.data,
            comments: comments.data
        }
    },
}
</script>

<style scoped></style>