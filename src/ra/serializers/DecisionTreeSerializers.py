import sklearn
from sklearn import tree
import re

def json_minify(string, strip_space=True):
    tokenizer = re.compile('"|(/\*)|(\*/)|(//)|\n|\r')
    end_slashes_re = re.compile(r'(\\)*$')

    in_string = False
    in_multi = False
    in_single = False

    new_str = []
    index = 0

    for match in re.finditer(tokenizer, string):

        if not (in_multi or in_single):
            tmp = string[index:match.start()]
            if not in_string and strip_space:
                # replace white space as defined in standard
                tmp = re.sub('[ \t\n\r]+', '', tmp)
            new_str.append(tmp)

        index = match.end()
        val = match.group()

        if val == '"' and not (in_multi or in_single):
            escaped = end_slashes_re.search(string, 0, match.start())

            # start of string or unescaped quote character to end string
            if not in_string or (escaped is None or len(escaped.group()) % 2 == 0):
                in_string = not in_string
            index -= 1 # include " character in next catch
        elif not (in_string or in_multi or in_single):
            if val == '/*':
                in_multi = True
            elif val == '//':
                in_single = True
        elif val == '*/' and in_multi and not (in_string or in_single):
            in_multi = False
        elif val in '\r\n' and not (in_multi or in_string) and in_single:
            in_single = False
        elif not ((in_multi or in_single) or (val in ' \r\n\t' and strip_space)):
            new_str.append(val)

    new_str.append(string[index:])
    return ''.join(new_str)


def DecisionTreeSerializer(decision_tree, feature_names=None, minify=True):
 
  js = ""
 
  def node_to_str(tree, node_id, criterion):
    if not isinstance(criterion, sklearn.tree.tree.six.string_types):
      criterion = "impurity"
 
    value = tree.value[node_id]
    if tree.n_outputs == 1:
      value = value[0, :]
 
    jsonValue = ', '.join([str(x) for x in value])
 
    if tree.children_left[node_id] == sklearn.tree._tree.TREE_LEAF:
      return '"samples": %s, "value": [%s], "error": %s ,"type":"leaf"' \
             % (tree.n_node_samples[node_id],
                jsonValue,
                tree.impurity[node_id])
    else:
      if feature_names is not None:
        feature = feature_names[tree.feature[node_id]]
      else:
        feature = tree.feature[node_id]
 
      if "=" in feature:
        ruleType = "="
        ruleValue = "false"
      else:
        ruleType = "<="
        ruleValue = "%.4f" % tree.threshold[node_id]
 
      return '"label": "%s %s %s", "error": %s, "samples": %s, "type":"split"' \
             % (feature,
                ruleType,
                ruleValue,
                #criterion,
                tree.impurity[node_id],
                tree.n_node_samples[node_id])
 
  def recurse(tree, node_id, criterion, parent=None, depth=0):
    tabs = "  " * depth
    js = ""
 
    left_child = tree.children_left[node_id]
    right_child = tree.children_right[node_id]
 
    js = js + "\n" + \
         tabs + "{\n" + \
         tabs + "  " + node_to_str(tree, node_id, criterion)
 
    if left_child != sklearn.tree._tree.TREE_LEAF:
      js = js + ', "children": {'
      js = js + "\n" + \
           tabs + '  "0": ' + \
           recurse(tree, \
                   left_child, \
                   criterion=criterion, \
                   parent=node_id, \
                   depth=depth + 1) + ",\n" + \
           tabs + '  "1": ' + \
           recurse(tree, \
                   right_child, \
                   criterion=criterion, \
                   parent=node_id,
                   depth=depth + 1) + "}"
 
    js = js + tabs + "\n" + \
         tabs + "}"
 
    return js
 
  if isinstance(decision_tree, sklearn.tree.tree.Tree):
    js = js + recurse(decision_tree, 0, criterion="impurity")
  else:
    js = js + recurse(decision_tree.tree_, 0, criterion=decision_tree.criterion)
  if (minify == True):
    return json_minify(js)
  else :
    return js



def DescisionTreeSerializerForSunburst(decision_tree, feature_names=None,minify=True):
  js = ""
 
  def node_to_str(tree, node_id, criterion):
    if not isinstance(criterion, sklearn.tree.tree.six.string_types):
      criterion = "impurity"
 
    value = tree.value[node_id]
    if tree.n_outputs == 1:
      value = value[0, :]
 
    jsonValue = ', '.join([str(x) for x in value])
 
    if tree.children_left[node_id] == sklearn.tree._tree.TREE_LEAF:
      return '"samples": %s, "value": %s, "error": %s ,"type":"leaf"' \
             % (tree.n_node_samples[node_id],
                jsonValue,
                tree.impurity[node_id])
    else:
      if feature_names is not None:
        feature = feature_names[tree.feature[node_id]]
      else:
        feature = tree.feature[node_id]
 
      if "=" in feature:
        ruleType = "="
        ruleValue = "false"
      else:
        ruleType = "<="
        ruleValue = "%.4f" % tree.threshold[node_id]
 
      return '"predicate": { "field" : "%s", "operator" : "%s", "value": %s}, "error": %s, "samples": %s, "type":"split"' \
             % (feature,
                ruleType,
                ruleValue,
                tree.impurity[node_id],
                tree.n_node_samples[node_id])
 
  def recurse(tree, node_id, criterion, parent=None, depth=0):
    tabs = "  " * depth
    js = ""
 
    left_child = tree.children_left[node_id]
    right_child = tree.children_right[node_id]
 
    js = js + "\n" + \
         tabs + "{\n" + \
         tabs + "  " + node_to_str(tree, node_id, criterion)
 
    if left_child != sklearn.tree._tree.TREE_LEAF:
      js = js + ', "children": {'
      js = js + "\n" + \
           tabs + '  "0": ' + \
           recurse(tree, \
                   left_child, \
                   criterion=criterion, \
                   parent=node_id, \
                   depth=depth + 1) + ",\n" + \
           tabs + '  "1": ' + \
           recurse(tree, \
                   right_child, \
                   criterion=criterion, \
                   parent=node_id,
                   depth=depth + 1) + "}"
 
    js = js + tabs + "\n" + \
         tabs + "}"
 
    return js
 
  if isinstance(decision_tree, sklearn.tree.tree.Tree):
    js = js + recurse(decision_tree, 0, criterion="impurity")
  else:
    js = js + recurse(decision_tree.tree_, 0, criterion=decision_tree.criterion)
  if (minify == True):
    return json_minify(js)
  else :
    return js
  
