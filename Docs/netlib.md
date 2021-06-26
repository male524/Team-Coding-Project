# netlib

## Table of Contents

* [Terms Used](#terms-used)
* [Other Things to Note](#other-things-to-note)
* [Class: netlib.Queue](#class-netlibqueue)
	* [new netlib.Queue([itemList])](#new-netlibqueueitemlist)
	* [queue.enqueue(item)](#queueenqueueitem)
	* [queue.dequeue()](#queuedequeue)
	* [queue.isEmpty()](#queueisempty)
	* [queue.hasMore()](#queuehasmore)
	* [queue.itemCount()](#queueitemcount)
* [Class: netlib.DataNode](#class-netlibdatanode)
	* [new netlib.DataNode([childData[, userData[, isParentNode]]])](#new-netlibdatanodechilddata-userdata-isparentnode)
	* [datanode.toJSON()](#datanodetojson)
	* [datanode.addNode(name,node)](#datanodeaddnodenamenode)
	* [datanode.addData(name, data[, userData])](#datanodeadddataname-data-userdata)
	* [datanode.addObject(name,obj)](#datanodeaddobjectnameobj)
	* [datanode.forChildren(callback)](#datanodeforchildrencallback)
	* [datanode.getData()](#datanodegetdata)
	* [datanode.getChild(name)](#datanodegetchildname)
	* [datanode.hasChild(name)](#datanodehaschildname)
	* [datanode.setObjectIfIncluded(name,obj)](#datanodesetobjectifincludednameobj)
	* [dataNode.setDataIfIncluded(name,parent,child)](#datanodesetdataifincludednameparentchild)

## Terms Used

* Something: Some piece of data in javascript (function, object, string, integer, boolean, etc.)
* JSomething: Some piece of data in javascript that can be translated into a JSON string. (not functions, undefined, etc. or anything containing them)

* non-parent DataNode: a DataNode that is not marked as a parent DataNode, and may only contain an arbitrary JSomething as its child data.
* parent DataNode: a DataNode that is marked as a parent DataNode, and may only contain a set of DataNodes as its child data.

## Other Things to Note

This is an incomplete documentation of netlib.js, and may be poorly written in some parts. If you are confused as to how to do something with the library, ask me.

## Class: netlib.Queue

This class is a queue. It is specific to netlib.

### new netlib.Queue([itemList])

* `itemList` {Array} Inital elements inside the queue. First item is the first to be dequeued. Defaults to `[]` if unspecified.

Creates a new queue.

### queue.enqueue(item)

* `item` {Something} Thing to enqueue.

Enqueues something into the queue.

### queue.dequeue()

Returns the first item in the queue, and dequeues it.

### queue.isEmpty()

Returns a boolean, true if the queue has no more items in it, false otherwise.

### queue.hasMore()

Returns a boolean, true, if the queue has more items, false otherwise. Opposite to `queue.isEmpty`.

### queue.itemCount()

Returns an integer, specifying the number of items still left in the queue.

## Class: netlib.DataNode

This is a class for representing a hierarchical/tree like data structure. This data can then be converted to a javascript object representable as JSON, which can then be transfered over a network.

### new netlib.DataNode([childData[, userData[, isParentNode]]])

* `childData` {Object/JSomething} Child data of the DataNode. Defaults to `{}` if unspecified. See description below.
* `userData` {JSomething} User specified data associated with the DataNode. Defaults to `{}` if unspecified.
* `isParentNode` {Boolean/Null} Specifies whether or not the DataNode is a parent node. Defaults to `null` if unspecified. See description below.

Creates a new `DataNode`.

DataNodes can either contain data representable as JSON, or can contain a set of other DataNodes that are children of it. Both of these are specified by `childData`.

`isParentNode` specifies whether or not the DataNode is storing a collection of data representable in JSON (`isParentNode` is `false`) or if it is storing other DataNodes that are children of it (`isParentNode` is `true`).
If `isParentNode` is `null`, then it assumes what the DataNode is supposed to be. If `childData` is an object that is not `null`, then it assumes `isParentNode` to be true. Otherwise, it assumes it to be `false`.
If `isParentNode` is either specified or assumed incorrectly, then undefined behavior may result.

### datanode.toJSON()

Takes the DataNode called and everything it is a parent of and packages it up into a javascript object that can be converted into a JSON string.

### datanode.addNode(name,node)

* `name` {String} The name of the node to be added.
* `node` {DataNode} The node to be added.

Adds a DataNode as a child of the DataNode called.

Calling this on a DataNode with `isParentNode` as `false` leads to undefined behavior.
Calling this on a DataNode with a child DataNode of the same name leads to the child DataNode being overwriten. This is not recommended.

### datanode.addData(name, data[, userData])

* `name` {String} Name of DataNode to add.
* `data` {JSomething} Data in DataNode to add.
* `userData` {JSomething} UserData in DataNode to add.

Adds a DataNode with `isParentNode` as `false` to the DataNode called, with `data` as `childData`.

Equivalent to
```Javascript
dataNode.addNode(name, new lib.DataNode(data,userData,false))
```

### datanode.addObject(name,obj)

* `name` {String} Name of data added from object.
* `obj` {Object w/ .getData()} Object to have its data added.

Takes the DataNode returned from `obj.getData()` and adds it to the DataNode called.
`obj.getData()` must return a DataNode.

Equivalent to
```Javascript
this.addNode(name,obj.getData())
```

### datanode.forChildren(callback)

* `callback` {Function} Callback called for each child node.

For each child node, calls `callback(name,childNode)`, where name is the name of the child node, and childNode is the childNode itself.
Throws `"netlib.DataNode.forChildren: this is a parent node"` if called on a non-parent DataNode.

### datanode.getData()

Returns the child data of a DataNode. Only meant to be used on non-parent DataNodes.

### datanode.getChild(name)

* `name` {String} The name of the child DataNode requested.

Returns the child of a parent DataNode by name. Only meant to be used on parent DataNodes.

### datanode.hasChild(name)

* `name` {String} The name of of the child DataNode queried.

Returns whether or not the DataNode has a child DataNode with the name in question. Using this on a non-parent DataNode leads to undefined behavior.

### datanode.setObjectIfIncluded(name,obj)

* `name` {String} The name of the DataNode in question.
* `obj` {Object w/ .setData()} The object to have its data set.

If the DataNode called has a child DataNode with the name specified by `name`, then `obj.setData(dataNode)` gets called, with `dataNode` as the child DataNode specified by `name`. Calling this on a non-parent DataNode leads to undefined behavior.

### dataNode.setDataIfIncluded(name,parent,child)

* `name` {String} The name of the DataNode in question.
* `parent` {Object} The parent object of the data to be set.
* `child` {String/Integer} The name of the data in `parent` that is to be set.

If the DataNode called has a child DataNode with the name specified by `name`, then `parent[child]` is set to the child data of the child DataNode specified.