
package com.company;

import java.util.Arrays;

public class MyHashMap<K, V> {
 public static class Node<K, V> {
  final K key;
  V value;
  Node<K, V> next;
  Node(K key, V value) {
   this.key = key;
   this.value = value;
  }
  
  public K getKey() {
   return key;
  }
  
  public V getValue() {
   return value;
  }
  
  public void setValue(V value) {
   this.value = value;
  }
 }
 
 private static final int DEFAULT_CAPACITY = 16;
 private static final float DEFAULT_LOAD_FACTOR = 0.75f;
 private static final int SCALE_FACTOR = 2;
 
 private Node<K, V>[] array;
 private int size; // how many key-value pairs are actually stored in the HashMap
 private final float loadFactor; // determine when to rehash
 
 public MyHashMap() {
  this(DEFAULT_CAPACITY, DEFAULT_LOAD_FACTOR);
 }
 
 @SuppressWarnings("unchecked")
 public MyHashMap(int cap, float loadFactor) {
  if (cap <= 0) {
   throw new IllegalArgumentException("capacity can not be <= 0");
  }
  // java 不允许generic的array -> 强制cast
  this.array = (Node<K, V>[]) (new Node[cap]);
  this.size = 0;
  this.loadFactor = loadFactor;
 }
 
 public int size() {
  return size;
 }
 
 public boolean isEmpty() {
  return size == 0;
 }
 
 public void clear() {
  Arrays.fill(array, null);
 }
 
 // non-negative 
 private int hash(K key) {
  // 规定null永远放在0号bucket
  if (key == null) {
   return 0;
  }
  // 保证hash不为负
  return key.hashCode() & 0X7FFFFFFF;
 }
 
 // 决定放在第几个bucket
 private int getIndex(K key) {
  return hash(key) % array.length;
 }
 
 private boolean equalsValue(V v1, V v2) {
  if (v1 == null && v2 == null) {
   return true;
  }
  if (v1 == null || v2 == null) {
   return false;
  }
  return v1.equals(v2);
 }
 
 // O(n) implementation
 public boolean containsValue(V value) {
  if(isEmpty()) {
   return false;
  }
  // 遍历每一个bucket中的linked-list
  for (Node<K, V> node : array) {
   while (node != null) {
    if (equalsValue(node.value, value)) {
     return true;
    }
    node = node.next;
   }
  }
  return false;
 }
 
 private boolean equalsKey(K k1, K k2) {
  if (k1 == null && k2 == null) {
   return true;
  }
  if (k1 == null || k2 == null) {
   return false;
  }
  return k1.equals(k2);
 }
 
 public boolean containsKey(K key) {
  int index = getIndex(key);
  Node<K, V> node = array[index];
  while (node != null) {
   if (equalsKey(key, node.key)) {
    return true;
   }
   node = node.next;
  }
  return false;
 }
 
 // if key doesn't exist in the hashMap, return null
 public V get(K key) {
  int index = getIndex(key);
  Node<K, V> node = array[index];
  while (node != null) {
   if (equalsKey(node.key, key)) {
    return node.value;
   }
   node = node.next;
  }
  return null;
 }
 
 public V put(K key, V value) {
  int index = getIndex(key);
  Node<K, V> head = array[index];
  Node<K, V> node = head;
  while (node != null) {
   if (equalsKey(node.key, key)) {
    V result = node.value;
    node.value = value;
    return result;
   }
   node = node.next;
  }
  // this entry is not in the HashMap
  // append head
  Node<K, V> newNode = new Node<>(key, value);
  newNode.next = head;
  array[index] = newNode;
  size++;
  if (needRehashing()) {
   rehashing();
  }
  return null;
 }
 
 private boolean needRehashing() {
  float ratio = (size + 0.0f) / array.length;
  return ratio >= loadFactor;
 }
 
 @SuppressWarnings("unchecked")
 private void rehashing() {
  Node<K, V>[] oldArray = array;
  array = (Node<K, V>[]) (new Node[array.length * SCALE_FACTOR]);
  // 对原来的每一个Node都重新分配
  for (Node<K, V> node : oldArray) {
   while (node != null) {
    Node<K, V> next = node.next;
    int index = getIndex(node.key);
    node.next = array[index];
    array[index] = node;
    node = next;
   }
  }
 }
 
 public V remove(K key) {
  // get index
  // delete 
  // size--
  int index = getIndex(key);
  Node<K, V> node = array[index];
  Node<K, V> prev = null;
  while (node != null) {
   if (equalsKey(node.key, key)) {
    if (prev != null) {
     prev.next = node.next;
    } else {
     array[index] = node.next;
    }
    size--;
    return node.value;
   }
   prev = node;
   node = node.next;
  }
  return null;
 }
 
 public static void main(String args[]) {
  MyHashMap<String, Integer> map = new MyHashMap<String, Integer>(4, 0.75f);
  map.put("1", 1);
  map.put("2", 2);
  map.put("3", 3);
  map.put("4", 4);
  System.out.println(map.containsKey("2"));
  System.out.println(map.containsKey("5"));
  map.remove("2");
  System.out.println(map.containsKey("2"));
  System.out.println(map.containsValue(2));
  System.out.println(map.containsValue(3));
  System.out.println(map.get("2"));
  System.out.println(map.get("3"));
 }

}
