https://docs.stirlingpdf.com/Installation/Docker%20Install


https://hub.docker.com/r/frooodle/s-pdf/


Stirling PDF的latest-fat、latest-ultra-lite、latest三个镜像版本有以下区别：

### 功能完整性
- **latest-fat**：功能最全面，包含了Stirling PDF的所有功能，如完整的PDF转换、编辑、OCR识别、文件压缩等功能。支持将PDF转换为Word、Excel、图像等多种格式，还能进行复杂的编辑操作。
- **latest-ultra-lite**：功能相对精简，不包含libre、python、opencv、ocrmypdf等技术，在操作方面不支持compress-pdf、extract-image-scans、ocr-pdf、pdf-to-pdfa等功能。
- **latest**：通常是默认的推荐版本，功能完整性介于latest-fat和latest-ultra-lite之间，能满足大多数用户的常见需求，包含了核心的PDF处理功能，如基本的拆分、合并、转换、添加水印等。

### 镜像大小
- **latest-fat**：由于包含了完整的功能和相关依赖，镜像文件体积最大。
- **latest-ultra-lite**：去除了很多非核心的功能和依赖，镜像文件体积最小，如之前版本中stirling-pdf-ultra-lite为177mb。
- **latest**：镜像大小适中，在保证一定功能的同时，不会占用过多的存储空间。

### 适用场景
- **latest-fat**：适合对PDF处理功能要求全面，需要进行大量复杂操作，如企业的文档处理部门、专业的图文处理机构等。
- **latest-ultra-lite**：适用于对功能需求不高，只需要进行基本的PDF操作，且对存储空间有限制的场景，如个人用户在配置较低的设备上使用。
- **latest**：适用于大多数普通用户和常见场景，既能满足日常的PDF处理需求，又不会过于占用资源和空间。

### 部署与运行性能
- **latest-fat**：因为功能多、依赖多，部署过程相对复杂，对服务器的硬件资源要求较高，运行时可能会占用较多的CPU、内存等资源。
- **latest-ultra-lite**：部署简单，对硬件资源要求低，在性能较差的设备上也能相对流畅地运行。
- **latest**：部署和运行性能介于两者之间，能在一般的硬件配置上良好运行，部署难度也相对适中。
