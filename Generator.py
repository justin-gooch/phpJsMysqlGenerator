tableColumns = input('please enter table columns separated by ":" :');
columnArray = tableColumns.split(":");

print "=====================php==================="
print "$returnArray = array();"
for column in columnArray:
	print "$" + column + "Array = array();";

print "$sql = 'insert sql statement here'; "
print "foreach($db->query($sql) as $row)";
print "{"
for column in columnArray:
	print "array_push($"+column+"Array, $row['"+column+"']);"
print "}";

for column in columnArray:
	print "$returnArray['"+column+"'] = $"+column+"Array;"
print "return $returnArray";
print "====================js=================="

print "$.post('dbCalls.php', {requestType: 'fetchRequestTyle', +searchVariable: 'searchVariable'})";
print "	.done(function(data))"
print "	{"
print "arrays=jQuery.parseJson(data);"
for column in columnArray:
	print column+" =arrays."+column;
print " });"
print"});"