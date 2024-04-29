<template>
  <div>
    <div class="card my-4">
      <h5 class="card-header">Прокомментируй:</h5>
      <div class="card-body">
        <form>
          <div class="form-group">
            <textarea class="form-control" rows="3"></textarea>
          </div>
          <button type="submit" class="btn btn-dark">Отправить</button>
        </form>
      </div>
    </div>
    <div class="media mb-4" v-for="comment in comments" :key="comment.id">
      <img class="d-flex mr-3 rounded-circle" src="http://placehold.it/50x50" alt="">
      <div class="media-body">
        <h5 class="mt-0">{{comment.username}}</h5>
        {{comment.text}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['comments'],
}
</script>

<style scoped>

</style>