// Singly Linked List implementation
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  append(value) {
    const node = new Node(value);
    if (!this.head) { this.head = node; }
    else {
      let current = this.head;
      while (current.next) current = current.next;
      current.next = node;
    }
    this.size++;
  }

  toArray() {
    const result = [];
    let current = this.head;
    while (current) { result.push(current.value); current = current.next; }
    return result;
  }
}

const list = new LinkedList();
list.append(1); list.append(2); list.append(3);
console.log(list.toArray()); // [1, 2, 3]
