var defaultThreads = [
    {
        id: 1,
        title: "Thread 1",
        author: "Student 1",
        date: Date.now(),
        content: "Thread content",
        comments: [
            {
                author: "Student 2",
                date: Date.now(),
                content: "Hey there"
            },
            {
                author: "Student 1",
                date: Date.now(),
                content: "Hey to you too"
            }
        ]
    },
    {
        id: 2,
        title: "Thread 2",
        author: "Student 1",
        date: Date.now(),
        content: "Thread content 2",
        comments: [
            {
                author: "Student 2",
                date: Date.now(),
                content: "Hey there"
            },
            {
                author: "Student 3",
                date: Date.now(),
                content: "Hey to you too"
            }
        ]
    }
]

var threads = defaultThreads
if (localStorage && localStorage.getItem('threads')) {
    threads = JSON.parse(localStorage.getItem('threads'));
} else {
    threads = defaultThreads;
    localStorage.setItem('threads', JSON.stringify(defaultThreads));
}