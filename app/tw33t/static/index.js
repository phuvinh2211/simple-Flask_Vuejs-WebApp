Vue.component('get-tweets', {
  data: function() {
    return {
      user_screen: '',
      latest_tweets: [],
      tweet: {},
      input_valid: true
    }
  },

  methods: {
    fetchTweets: function() {

      // If input is filled, then get request to the server
      if (!/\S/.test(this.user_screen) == '') {
        this.input_valid = true
        const url = '/get_tweets/' + this.user_screen + '/';

        axios.get(url)
        .then (response => {
          this.latest_tweets = response.data;
        })
      }

      // If no, prompt the message error back to user
      else {
        this.input_valid = false;
      }
    }
  },

  template: `
    <div class="center user-input-wrapper">
      <input v-model="user_screen" class="user-input" placeholder="Typing your twitter handle or someone here...">

      <div class="submit-button-wrapper">
        <button v-on:click="fetchTweets" class="submit-button">tweets</button>
      </div>

      <div v-if="!input_valid" class="aler-error">Oop!!! You did not type anything above.</div>
      <div v-else>
        <div class="tweet-list-wrapper">
          <div v-for="tweet in latest_tweets">
            <div class="tweet-li-date"> {{ tweet.creation_date }} </div>
            <div class="tweet-list-detail">{{ tweet.content }}</div>
          </div>
        </div>
      </div>
    </div>
    `
})

new Vue({ el: '#vue-tweets-app' })
