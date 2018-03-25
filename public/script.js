function AssignDataToLink() {
  	var csv = "Id,Value\n1,Muhammad\n";
		var data = new Blob([csv]);
		var downloadLink = document.getElementById("aDownloadCsv");

		downloadLink.href = URL.createObjectURL(data);
}

function ExportData() {
  	var csv = "Id, Value\n1,Muhammad\n";
		var data = new Blob([csv]);
		var downloadLink = document.getElementById("aDownloadCsv2");

		if (downloadLink == null) {
		  downloadLink = document.createElement('a');
		  downloadLink.setAttribute('download', 'DownloadedFile.csv');
		  downloadLink.setAttribute('id', 'aDownloadCsv2');

      document.body.appendChild(downloadLink);
		}

		downloadLink.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(data));
		downloadLink.href = URL.createObjectURL(data);

		downloadLink.style.display = 'none';
		downloadLink.click();
}
