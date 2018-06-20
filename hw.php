<?php
include_once('./simple_html_dom.php');
	
$url = "https://store.steampowered.com/search/?filter=globaltopseller&os=win";
$html = file_get_html($url);

$count = 0;
$rank = [];	

foreach($html->find('span.title') as $element) {
	$count ++;
	$title = $element->innertext;
	echo "$count $title\n";
	array_push($rank, $title);
}
if ($title == "PLAYERUNKNOWN'S BATTLEGROUNDS" and "Dead by Daylight") {
	echo "있음";
}
else {
	printf("없음", array_search("Raft", $rank)+1);
}
?>