tableColumns = input('please enter table columns separated by ":" :');
columnArray = tableColumns.split(":");

print "=====================php==================="
print "\t$returnArray = array();"
for column in columnArray:
	print "\t$" + column + "Array = array();";

print "\t$sql = 'insert sql statement here'; "
print "\tforeach($db->query($sql) as $row)";
print "\t{"
for column in columnArray:
	print "\t\tarray_push($"+column+"Array, $row['"+column+"']);"
print "\t}";

for column in columnArray:
	print "\t$returnArray['"+column+"'] = $"+column+"Array;"
print "\treturn $returnArray";
print "====================js=================="

print "\t$.post('dbCalls.php', {requestType: 'fetchRequestTyle', +searchVariable: 'searchVariable'})";
print "	\t\t.done(function(data))"
print "	\t\t{"
print "\t\t\tarrays=jQuery.parseJson(data);"
for column in columnArray:
	print "\t\t\t" +column+" =arrays."+column;
print " \t\t});"
 