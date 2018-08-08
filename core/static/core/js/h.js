function print_r(o){
    alert(JSON.stringify(o, null, 4));
}

function printObject(o) {
    var out = '';
    for (var p in o) {
      out += p + ': ' + o[p] + '\n';
    }
    alert(out);
  }
  
  function print_r2(printthis, returnoutput) {
      var output = '';
  
      if($.isArray(printthis) || typeof(printthis) == 'object') {
          for(var i in printthis) {
              output += i + ' : ' + print_r(printthis[i], true) + '\n';
          }
      }else {
          output += printthis;
      }
      if(returnoutput && returnoutput == true) {
          return output;
      }else {
          alert(output);
      }
  }