$("#search").click(function(){
  search()
})

async function searchAPI(){
  const response = await fetch("/search");
  return response.json()

}

function search(){
  searchAPI().then(function(data){
    console.log(data);
  })
}

search();
