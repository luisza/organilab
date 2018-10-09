
function do_sortable(){
	  $("ul.sortableself").sortable({group: 'nested'});
}

function addRow() {
	sk=$("<tr> </tr>");
	if($('#mytab tr:last td').length>0){
		$('#mytab tr:last td').each(function(i, e){
			var inp = "<td>"+$("#addshelfproto").html()+"</td>";
			inp=inp.replace(/ROW/g, ""+document.numberRow);
			inp=inp.replace(/COL/g, ""+i);
			sk.append(inp);
		});
	} else {
		var inp = "<td>"+$("#addshelfproto").html()+"</td>";
		inp=inp.replace(/ROW/g, ""+document.numberRow);
		inp=inp.replace(/COL/g, ""+document.numberCol);	
		sk.append(inp);
		document.numberCol++;
	}
	$('#mytab').append(sk);
	document.numberRow++;
	do_sortable();
}

function addColumn() {
	if($('#mytab tr').length>0){
		$('#mytab tr').each(function(i, e){
			var inp = "<td>"+$("#addshelfproto").html()+"</td>";
			inp=inp.replace(/ROW/g, ""+i);
			inp=inp.replace(/COL/g, ""+document.numberCol);	
			$(e).append(inp);
		});			
	}else{
		var inp = "<td>"+$("#addshelfproto").html()+"</td>";
		inp=inp.replace(/ROW/g, ""+document.numberRow);
		inp=inp.replace(/COL/g, ""+document.numberCol);		
		$('#mytab').append("<tr>"+inp+"</tr>");	
		document.numberRow++;	
	}
	document.numberCol++;
	do_sortable();
}


function deleteRows() {
	$('#mytab tr').last().remove();
	document.numberRow--;
	do_sortable();
}

// delete table columns with index greater then 0
function deleteColumns() {
	$('#mytab tr').each(function(i, e){
		$(e).find("td:last").remove();
			
		});
		document.numberCol--;
		do_sortable();
}

function closeModal(){
	$("#createshelfmodal").modal("hide");
}

function processResponse(data) {
	$("#shelfmodalbody").html(data);
	activemodal = $("#createshelfmodal").modal('show');
}


function createconfigdata(){
  var dev = '[';
  var trs =$("#mytab tr");
  for (var x=0; x<trs.length; x++){
    dev += '[';
    var tds = $(trs[x]).find('td');
    for (var y=0; y<tds.length; y++){
      dev+='[';
      var inp = $(tds[y]).find("li");
      for (var z=0; z<inp.length; z++){
        dev += $(inp[z]).data('id');
        if(!(z+1==inp.length)) dev+=',';
      }
      dev+=']';
       if(!(y+1==tds.length)) dev+=',';
    }
    dev += ']';
    if(!(x+1==trs.length)) dev+=',';
  }
  return dev+']';
}

function save_form(){
	$('form').submit(
		function(event){
			console.log(createconfigdata());
			$("#id_dataconfig").val(createconfigdata());
	});
	
}

save_form();
do_sortable();