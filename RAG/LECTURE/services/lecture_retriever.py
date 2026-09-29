from app.retrieval.database import collection
from app.retrieval.lecture_retriever_core import lecture_retrieve


class LectureRetriever:
    """
    Adapter between Wael's Lecture Retriever and our
    existing Lecture Engine.

    Wael owns the retrieval logic.

    This class only provides the interface expected by
    our Lecture Engine.
    """

    def __init__(self):
        self.collection = collection

    # ======================================================
    # LESSON MATERIAL
    # ======================================================

    def get_lesson_material(self, course, lesson):
        """
        Return all concept chunks for a lesson.

        This is used once when starting a lecture so that
        LessonParser can build the ordered concept list.
        """

        results = self.collection.get(
            where={
                "$and": [
                    {"course": course},
                    {"lesson": lesson},
                    {"content_type": "concept"}
                ]
            }
        )

        chunks = []

        for i in range(len(results["ids"])):

            metadata = results["metadatas"][i]

            chunks.append({
                "chunk_id": results["ids"][i],
                "text": results["documents"][i],
                "page": metadata.get("page"),
                "course": metadata.get("course"),
                "lesson": metadata.get("lesson"),
                "concept": metadata.get("concept"),
                "document": metadata.get("document"),
                "section": metadata.get("section"),
                "concept_index": metadata.get("concept_index"),
                "chunk_index": metadata.get("chunk_index"),
                "content_type": metadata.get("content_type")
            })

        chunks.sort(
            key=lambda chunk: (
                chunk["concept_index"]
                if chunk["concept_index"] is not None
                else 999999,

                chunk["chunk_index"]
                if chunk["chunk_index"] is not None
                else 999999
            )
        )

        return chunks

    # ======================================================
    # SINGLE CONCEPT MATERIAL
    # ======================================================

    def get_concept_material(
        self,
        course,
        lesson,
        concept,
        top_k=5
    ):
        """
        Uses Wael's retrieval function to retrieve the
        chunks belonging to one specific concept.
        """

        return lecture_retrieve(
            collection=self.collection,
            course=course,
            lesson=lesson,
            concept=concept,
            top_k=top_k
        )