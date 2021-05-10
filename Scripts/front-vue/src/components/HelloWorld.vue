<template>
<div>
  <md-card class="md-accent" md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">PID</div>
          <div class="md-subhead">Personal Information Detection</div>
        </md-card-header>

        <md-card-content>
          AI 기반 개인정보 검출
        </md-card-content>

        <md-card-actions>
          <md-button @click="goto('/pi/uploadfiles')">Try</md-button>
        </md-card-actions>

      </md-ripple>
    </md-card>

<md-card>
      <md-card-media-cover md-text-scrim>
        <md-card-media md-ratio="16:9">
          <img src="@/assets/img/ocr_logo.jpg" alt="Skyscraper">
        </md-card-media>

        <md-card-area>
          <md-card-header>
            <span class="md-title">OCR</span>
            <span class="md-subhead">Optical Character Recognition</span>
          </md-card-header>

          <md-card-actions>
            <md-button>Show</md-button>
            <md-button>Try</md-button>
          </md-card-actions>
        </md-card-area>
      </md-card-media-cover>
</md-card>

</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
      goto(url) {
        this.$router.push(url);
      },
  }
}
</script>


<style lang="scss" scoped>


.md-card {
  width: 320px;
  height: 180px;
  margin: 4px;
  display: inline-block;
  vertical-align: top;
  }
</style>
