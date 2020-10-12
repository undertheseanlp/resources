$("#search").click(function(){
  search()
})

async function searchAPI(){
  const response = await fetch("/search");
  return response.json()

}

class Sentence {
  constructor(domId, content) {
    this.dom = "#" + domId;
    this.articleDom = "#article-" + domId;
    this.sentIdDom = this.articleDom + " g.sentnum text"
    this.content = content;
    this.sentId = content.split("\n")[0].substring(12)
  }

  hide(){
    $(this.articleDom).hide()
  }

  updateSentIdDom(){
    $(this.sentIdDom).html(this.sentId)
  }
  show(){
    var content = this.content.replace("sent_id =", "sentence-label")
    console.log(content)
    $(this.dom).val(content)
    $(this.dom).trigger("keyup")
    setTimeout(this.updateSentIdDom.bind(this), 500)
  }
}

function search(){
  searchAPI().then(function(data){
  console.log("search")
    content = data["sent"] + "\n"
    sentence = new Sentence("input", content)
    sentence.show()

    sentence2 = new Sentence("input-2", content)
    sentence2.show()
  })
}


search()
