"""Model ORM untuk data mata kuliah."""

from sqlalchemy import Column, Integer, Text

from .meta import Base


class Matakuliah(Base):
    """Merepresentasikan satu baris data mata kuliah."""

    __tablename__ = "matakuliah"

    id = Column(Integer, primary_key=True)
    kode_mk = Column(Text, unique=True, nullable=False)
    nama_mk = Column(Text, nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)

    def to_dict(self):
        """Mengubah objek mata kuliah menjadi dictionary siap JSON.

        Return:
            dict: Seluruh atribut mata kuliah dalam bentuk dictionary.
        """
        return {
            "id": self.id,
            "kode_mk": self.kode_mk,
            "nama_mk": self.nama_mk,
            "sks": self.sks,
            "semester": self.semester,
        }
