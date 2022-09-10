function connect(){
  data = "hello there";
  const req = new XMLHttpRequest();
  req.open("POST","/echo");

  req.onreadystatechange = function(res){
    if (req.readyState == 4 && req.status == 200){
      var resp = req.responseText;
      console.log(resp);
    }
  }
  
  req.send(data);
}
