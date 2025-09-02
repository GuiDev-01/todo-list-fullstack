import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, FlatList } from 'react-native';
import React, { useState } from 'react';

export default function App() {
    // Estado para armazenar o texto do input
    // Em JavaScript usamos 'const' e colchetes [] para destructuring
    const [newTask, setNewTask] = useState('');
    
    // Estado para armazenar lista de tarefas
    const [tasks, setTasks] = useState([]);

    // Função para adicionar nova tarefa
    const addTask = () => {
        if (newTask.trim() !== '') {
            const newTaskObj = {
                id: Date.now(), // ID simples usando timestamp
                text: newTask,
                completed: false
            };
            setTasks([...tasks, newTaskObj]); // Spread operator para adicionar item
            setNewTask(''); // Limpar o input
        }
    
    };

    const deleteTask = (taskId) => {
        setTasks(tasks.filter(task => task.id !== taskId));
    };

    const toggleTask = (taskId) => {
        setTasks(tasks.map(task =>
            task.id === taskId ? { ...task, completed: !task.completed } : task
        ));
    };

    return (
        <View style={styles.container}>
            <StatusBar style="auto" />
            {/* Título */}
            <Text style={styles.title}>📱 Todo List</Text>

            {/* Campo para nova tarefa */}
            <View style={styles.inputContainer}>
                <TextInput
                    style={styles.input}
                    placeholder="Adicione uma nova tarefa..."
                    value={newTask}
                    onChangeText={setNewTask}
                />
                <TouchableOpacity style={styles.addButton} onPress={addTask}>
                    <Text style={styles.addButtonText}>+</Text>
                </TouchableOpacity>
            </View>

            {/* Lista de tarefas */}
            <FlatList
                data={tasks}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <View style={styles.taskItem}>
                        <TouchableOpacity 
                            style={styles.taskContent}
                            onPress={() => toggleTask(item.id)}
                        >
                            <Text style={[styles.taskText, item.completed && styles.completedTask]}>
                                {item.completed ? '✅ ' : '☐ '} {item.text}
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity 
                            style={styles.deleteButton}
                            onPress={() => deleteTask(item.id)}
                        >
                            <Text style={styles.deleteButtonText}>🗑️</Text>
                        </TouchableOpacity>
                    </View>
                )}
                style={styles.taskList}
                showsVerticalScrollIndicator={false}
                ListEmptyComponent={
                    <Text style={styles.emptyText}>Nenhuma tarefa ainda. Adicione uma!</Text>
                }
            />
        </View>        
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f5f5f5',
        paddingTop: 50,
        paddingHorizontal: 20,
    },
    title: {
        fontSize: 28,
        fontWeight: 'bold',
        textAlign: 'center',
        marginBottom: 30,
        color: '#333',
    },
    inputContainer: {
        flexDirection: 'row',
        marginBottom: 20,
    },
    input: {
        flex: 1,
        borderWidth: 1,
        borderColor: '#ddd',
        borderRadius: 8,
        paddingHorizontal: 15,
        paddingVertical: 12,
        fontSize: 16,
        backgroundColor: 'white',
        marginRight: 10,
    },
    addButton: {
        backgroundColor: '#007AFF',
        width: 50,
        height: 50,
        borderRadius: 25,
        justifyContent: 'center',
        alignItems: 'center',
    },
    addButtonText: {
        color: 'white',
        fontSize: 24,
        fontWeight: 'bold',
    },
    taskList: {
        flex: 1,
    },
    taskItem: {
        backgroundColor: 'white',
        padding: 15,
        borderRadius: 8,
        marginBottom: 10,
        borderLeftWidth: 4,
        borderLeftColor: '#007AFF',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    taskContent: {
        flex: 1,
    },
    taskText: {
        fontSize: 16,
        color: '#333',
    },
    completedTask: {
        textDecorationLine: 'line-through',
        color: '#999',
    },
    deleteButton: {
        padding: 8,
        marginLeft: 10,
    },
    deleteButtonText: {
        fontSize: 18,
        color: '#FF6B6B',
    },
    emptyText: {
        textAlign: 'center',
        color: '#999',
        fontSize: 16,
        marginTop: 50,
        fontStyle: 'italic',
    },
});